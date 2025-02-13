import { i as ie, a as A, r as le, g as ae, w as O } from "./Index-CFhkpE8A.js";
const E = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, j = window.ms_globals.ReactDOM.createPortal, ce = window.ms_globals.internalContext.useContextPropsContext, ue = window.ms_globals.antd.Badge;
var de = /\s/;
function fe(e) {
  for (var t = e.length; t-- && de.test(e.charAt(t)); )
    ;
  return t;
}
var me = /^\s+/;
function pe(e) {
  return e && e.slice(0, fe(e) + 1).replace(me, "");
}
var F = NaN, _e = /^[-+]0x[0-9a-f]+$/i, he = /^0b[01]+$/i, ge = /^0o[0-7]+$/i, be = parseInt;
function M(e) {
  if (typeof e == "number")
    return e;
  if (ie(e))
    return F;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = pe(e);
  var s = he.test(e);
  return s || ge.test(e) ? be(e.slice(2), s ? 2 : 8) : _e.test(e) ? F : +e;
}
var P = function() {
  return le.Date.now();
}, ye = "Expected a function", Ee = Math.max, we = Math.min;
function xe(e, t, s) {
  var i, o, n, r, l, u, p = 0, g = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = M(t) || 0, A(s) && (g = !!s.leading, a = "maxWait" in s, n = a ? Ee(M(s.maxWait) || 0, t) : n, b = "trailing" in s ? !!s.trailing : b);
  function m(d) {
    var y = i, S = o;
    return i = o = void 0, p = d, r = e.apply(S, y), r;
  }
  function w(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var y = d - u, S = d - p, D = t - y;
    return a ? we(D, n - S) : D;
  }
  function _(d) {
    var y = d - u, S = d - p;
    return u === void 0 || y >= t || y < 0 || a && S >= n;
  }
  function h() {
    var d = P();
    if (_(d))
      return x(d);
    l = setTimeout(h, f(d));
  }
  function x(d) {
    return l = void 0, b && i ? m(d) : (i = o = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), p = 0, i = u = o = l = void 0;
  }
  function c() {
    return l === void 0 ? r : x(P());
  }
  function C() {
    var d = P(), y = _(d);
    if (i = arguments, o = this, u = d, y) {
      if (l === void 0)
        return w(u);
      if (a)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return C.cancel = v, C.flush = c, C;
}
var Y = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ve = E, Ce = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, s) {
  var i, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Se.call(t, i) && !Oe.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: Ce,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Re.current
  };
}
L.Fragment = Ie;
L.jsx = Q;
L.jsxs = Q;
Y.exports = L;
var R = Y.exports;
const {
  SvelteComponent: Te,
  assign: U,
  binding_callbacks: z,
  check_outros: ke,
  children: Z,
  claim_element: $,
  claim_space: Le,
  component_subscribe: G,
  compute_slots: Pe,
  create_slot: Ne,
  detach: I,
  element: ee,
  empty: H,
  exclude_internal_props: K,
  get_all_dirty_from_scope: je,
  get_slot_changes: Ae,
  group_outros: We,
  init: Be,
  insert_hydration: T,
  safe_not_equal: De,
  set_custom_element_data: te,
  space: Fe,
  transition_in: k,
  transition_out: W,
  update_slot_base: Me
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ue,
  getContext: ze,
  onDestroy: Ge,
  setContext: He
} = window.__gradio__svelte__internal;
function q(e) {
  let t, s;
  const i = (
    /*#slots*/
    e[7].default
  ), o = Ne(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      o && o.l(r), r.forEach(I), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Me(
        o,
        i,
        n,
        /*$$scope*/
        n[6],
        s ? Ae(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : je(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (k(o, n), s = !0);
    },
    o(n) {
      W(o, n), s = !1;
    },
    d(n) {
      n && I(t), o && o.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, s, i, o, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), s = Fe(), n && n.c(), i = H(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(I), s = Le(r), n && n.l(r), i = H(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, s, l), n && n.m(r, l), T(r, i, l), o = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = q(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (We(), W(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      o || (k(n), o = !0);
    },
    o(r) {
      W(n), o = !1;
    },
    d(r) {
      r && (I(t), I(s), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function V(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function qe(e, t, s) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Pe(n);
  let {
    svelteInit: u
  } = t;
  const p = O(V(t)), g = O();
  G(e, g, (c) => s(0, i = c));
  const a = O();
  G(e, a, (c) => s(1, o = c));
  const b = [], m = ze("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = ae() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: a,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      b.push(c);
    }
  });
  He("$$ms-gr-react-wrapper", h), Ue(() => {
    p.set(V(t));
  }), Ge(() => {
    b.forEach((c) => c());
  });
  function x(c) {
    z[c ? "unshift" : "push"](() => {
      i = c, g.set(i);
    });
  }
  function v(c) {
    z[c ? "unshift" : "push"](() => {
      o = c, a.set(o);
    });
  }
  return e.$$set = (c) => {
    s(17, t = U(U({}, t), K(c))), "svelteInit" in c && s(5, u = c.svelteInit), "$$scope" in c && s(6, r = c.$$scope);
  }, t = K(t), [i, o, g, a, l, u, r, n, x, v];
}
class Ve extends Te {
  constructor(t) {
    super(), Be(this, t, qe, Ke, De, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, N = window.ms_globals.tree;
function Je(e, t = {}) {
  function s(i) {
    const o = O(), n = new Ve({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], J({
            createPortal: j,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== o), J({
              createPortal: j,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(s);
    });
  });
}
const Xe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ye(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = Qe(s, i), t;
  }, {}) : {};
}
function Qe(e, t) {
  return typeof t == "number" && !Xe.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = B(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(j(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      s.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let o = 0; o < i.length; o++) {
    const n = i[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = B(n);
      t.push(...l), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function Ze(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const X = ne(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: o
}, n) => {
  const r = re(), [l, u] = oe([]), {
    forceClone: p
  } = ce(), g = p ? !0 : t;
  return se(() => {
    var w;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ze(n, f), s && f.classList.add(...s.split(" ")), i) {
        const _ = Ye(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, c, C;
        (v = r.current) != null && v.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: x
        } = B(e);
        a = x, u(h), a.style.display = "contents", b(), (C = r.current) == null || C.appendChild(a);
      };
      f();
      const _ = xe(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", b(), (w = r.current) == null || w.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, g, s, i, n, o]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Je(({
  slots: e,
  ...t
}) => /* @__PURE__ */ R.jsx(R.Fragment, {
  children: /* @__PURE__ */ R.jsx(ue, {
    ...t,
    count: e.count ? /* @__PURE__ */ R.jsx(X, {
      slot: e.count
    }) : t.count,
    text: e.text ? /* @__PURE__ */ R.jsx(X, {
      slot: e.text
    }) : t.text
  })
}));
export {
  et as Badge,
  et as default
};
