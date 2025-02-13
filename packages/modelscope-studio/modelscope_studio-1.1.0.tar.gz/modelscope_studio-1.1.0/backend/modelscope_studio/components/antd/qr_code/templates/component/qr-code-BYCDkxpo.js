import { i as ce, a as j, r as ae, g as ue, w as S, b as de } from "./Index-BofpY_vj.js";
const y = window.ms_globals.React, re = window.ms_globals.React.useMemo, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, le = window.ms_globals.React.useEffect, W = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, D = window.ms_globals.internalContext.ContextPropsProvider, me = window.ms_globals.antd.QRCode;
var pe = /\s/;
function _e(e) {
  for (var t = e.length; t-- && pe.test(e.charAt(t)); )
    ;
  return t;
}
var he = /^\s+/;
function ge(e) {
  return e && e.slice(0, _e(e) + 1).replace(he, "");
}
var U = NaN, we = /^[-+]0x[0-9a-f]+$/i, be = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, Ee = parseInt;
function z(e) {
  if (typeof e == "number")
    return e;
  if (ce(e))
    return U;
  if (j(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = j(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ge(e);
  var o = be.test(e);
  return o || ye.test(e) ? Ee(e.slice(2), o ? 2 : 8) : we.test(e) ? U : +e;
}
var L = function() {
  return ae.Date.now();
}, Ce = "Expected a function", ve = Math.max, xe = Math.min;
function Re(e, t, o) {
  var i, s, n, r, l, u, p = 0, g = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = z(t) || 0, j(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? ve(z(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(d) {
    var b = i, I = s;
    return i = s = void 0, p = d, r = e.apply(I, b), r;
  }
  function E(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var b = d - u, I = d - p, M = t - b;
    return c ? xe(M, n - I) : M;
  }
  function _(d) {
    var b = d - u, I = d - p;
    return u === void 0 || b >= t || b < 0 || c && I >= n;
  }
  function h() {
    var d = L();
    if (_(d))
      return C(d);
    l = setTimeout(h, f(d));
  }
  function C(d) {
    return l = void 0, w && i ? m(d) : (i = s = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), p = 0, i = u = s = l = void 0;
  }
  function a() {
    return l === void 0 ? r : C(L());
  }
  function x() {
    var d = L(), b = _(d);
    if (i = arguments, s = this, u = d, b) {
      if (l === void 0)
        return E(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return x.cancel = v, x.flush = a, x;
}
var Y = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ie = y, Se = Symbol.for("react.element"), Oe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, ke = Ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Pe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Te.call(t, i) && !Pe.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Se,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: ke.current
  };
}
P.Fragment = Oe;
P.jsx = Z;
P.jsxs = Z;
Y.exports = P;
var k = Y.exports;
const {
  SvelteComponent: Le,
  assign: B,
  binding_callbacks: G,
  check_outros: Ne,
  children: $,
  claim_element: ee,
  claim_space: We,
  component_subscribe: H,
  compute_slots: je,
  create_slot: Ae,
  detach: R,
  element: te,
  empty: K,
  exclude_internal_props: Q,
  get_all_dirty_from_scope: Fe,
  get_slot_changes: Me,
  group_outros: De,
  init: Ue,
  insert_hydration: O,
  safe_not_equal: ze,
  set_custom_element_data: ne,
  space: Be,
  transition_in: T,
  transition_out: A,
  update_slot_base: Ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: He,
  getContext: Ke,
  onDestroy: Qe,
  setContext: qe
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Ae(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = te("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ee(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = $(t);
      s && s.l(r), r.forEach(R), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ge(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Me(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Fe(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (T(s, n), o = !0);
    },
    o(n) {
      A(s, n), o = !1;
    },
    d(n) {
      n && R(t), s && s.d(n), e[9](null);
    }
  };
}
function Ve(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = te("react-portal-target"), o = Be(), n && n.c(), i = K(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(R), o = We(r), n && n.l(r), i = K(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, o, l), n && n.m(r, l), O(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && T(n, 1)) : (n = q(r), n.c(), T(n, 1), n.m(i.parentNode, i)) : n && (De(), A(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      s || (T(n), s = !0);
    },
    o(r) {
      A(n), s = !1;
    },
    d(r) {
      r && (R(t), R(o), R(i)), e[8](null), n && n.d(r);
    }
  };
}
function V(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Je(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = je(n);
  let {
    svelteInit: u
  } = t;
  const p = S(V(t)), g = S();
  H(e, g, (a) => o(0, i = a));
  const c = S();
  H(e, c, (a) => o(1, s = a));
  const w = [], m = Ke("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _
  } = ue() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      w.push(a);
    }
  });
  qe("$$ms-gr-react-wrapper", h), He(() => {
    p.set(V(t));
  }), Qe(() => {
    w.forEach((a) => a());
  });
  function C(a) {
    G[a ? "unshift" : "push"](() => {
      i = a, g.set(i);
    });
  }
  function v(a) {
    G[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = B(B({}, t), Q(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = Q(t), [i, s, g, c, l, u, r, n, C, v];
}
class Xe extends Le {
  constructor(t) {
    super(), Ue(this, t, Je, Ve, ze, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ye(e, t = {}) {
  function o(i) {
    const s = S(), n = new Xe({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
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
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== s), J({
              createPortal: W,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function Ze(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function $e(e, t = !1) {
  try {
    if (de(e))
      return e;
    if (t && !Ze(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function et(e, t) {
  return re(() => $e(e, t), [e, t]);
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = rt(o, i), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function F(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = F(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = F(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function ot(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const st = oe(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = se(), [l, u] = ie([]), {
    forceClone: p
  } = fe(), g = p ? !0 : t;
  return le(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), ot(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = nt(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, a, x;
        (v = r.current) != null && v.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: C
        } = F(e);
        c = C, u(h), c.style.display = "contents", w(), (x = r.current) == null || x.appendChild(c);
      };
      f();
      const _ = Re(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function X(e, t) {
  return e ? /* @__PURE__ */ k.jsx(st, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function it({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ k.jsx(D, {
    params: s,
    forceClone: !0,
    children: X(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ k.jsx(D, {
    params: s,
    forceClone: !0,
    children: X(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const ct = Ye(({
  setSlotParams: e,
  slots: t,
  statusRender: o,
  ...i
}) => {
  const s = et(o);
  return /* @__PURE__ */ k.jsx(me, {
    ...i,
    statusRender: t.statusRender ? it({
      slots: t,
      setSlotParams: e,
      key: "statusRender"
    }) : s
  });
});
export {
  ct as QRCode,
  ct as default
};
