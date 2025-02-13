import { i as le, a as j, r as ce, g as ae, w as S, b as ue } from "./Index-BHhqCGfL.js";
const v = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, ie = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, de = window.ms_globals.antd.Image;
var me = /\s/;
function pe(e) {
  for (var t = e.length; t-- && me.test(e.charAt(t)); )
    ;
  return t;
}
var _e = /^\s+/;
function ge(e) {
  return e && e.slice(0, pe(e) + 1).replace(_e, "");
}
var D = NaN, he = /^[-+]0x[0-9a-f]+$/i, we = /^0b[01]+$/i, be = /^0o[0-7]+$/i, ve = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (le(e))
    return D;
  if (j(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = j(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ge(e);
  var o = we.test(e);
  return o || be.test(e) ? ve(e.slice(2), o ? 2 : 8) : he.test(e) ? D : +e;
}
var P = function() {
  return ce.Date.now();
}, ye = "Expected a function", Ee = Math.max, Ce = Math.min;
function xe(e, t, o) {
  var s, i, n, r, l, u, p = 0, h = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = G(t) || 0, j(o) && (h = !!o.leading, c = "maxWait" in o, n = c ? Ee(G(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(f) {
    var b = s, R = i;
    return s = i = void 0, p = f, r = e.apply(R, b), r;
  }
  function y(f) {
    return p = f, l = setTimeout(g, t), h ? m(f) : r;
  }
  function d(f) {
    var b = f - u, R = f - p, M = t - b;
    return c ? Ce(M, n - R) : M;
  }
  function _(f) {
    var b = f - u, R = f - p;
    return u === void 0 || b >= t || b < 0 || c && R >= n;
  }
  function g() {
    var f = P();
    if (_(f))
      return E(f);
    l = setTimeout(g, d(f));
  }
  function E(f) {
    return l = void 0, w && s ? m(f) : (s = i = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : E(P());
  }
  function x() {
    var f = P(), b = _(f);
    if (s = arguments, i = this, u = f, b) {
      if (l === void 0)
        return y(u);
      if (c)
        return clearTimeout(l), l = setTimeout(g, t), m(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return x.cancel = C, x.flush = a, x;
}
var Y = {
  exports: {}
}, T = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ie = v, Re = Symbol.for("react.element"), Se = Symbol.for("react.fragment"), ke = Object.prototype.hasOwnProperty, Oe = Ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Te = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) ke.call(t, s) && !Te.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Re,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Oe.current
  };
}
T.Fragment = Se;
T.jsx = Q;
T.jsxs = Q;
Y.exports = T;
var L = Y.exports;
const {
  SvelteComponent: Pe,
  assign: U,
  binding_callbacks: z,
  check_outros: Le,
  children: Z,
  claim_element: $,
  claim_space: Ne,
  component_subscribe: B,
  compute_slots: We,
  create_slot: je,
  detach: I,
  element: ee,
  empty: H,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Ae,
  get_slot_changes: Fe,
  group_outros: Me,
  init: De,
  insert_hydration: k,
  safe_not_equal: Ge,
  set_custom_element_data: te,
  space: Ue,
  transition_in: O,
  transition_out: A,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Be,
  getContext: He,
  onDestroy: Ke,
  setContext: qe
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = je(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      i && i.l(r), r.forEach(I), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && ze(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Fe(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ae(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (O(i, n), o = !0);
    },
    o(n) {
      A(i, n), o = !1;
    },
    d(n) {
      n && I(t), i && i.d(n), e[9](null);
    }
  };
}
function Ve(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = Ue(), n && n.c(), s = H(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(I), o = Ne(r), n && n.l(r), s = H(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && O(n, 1)) : (n = q(r), n.c(), O(n, 1), n.m(s.parentNode, s)) : n && (Me(), A(n, 1, 1, () => {
        n = null;
      }), Le());
    },
    i(r) {
      i || (O(n), i = !0);
    },
    o(r) {
      A(n), i = !1;
    },
    d(r) {
      r && (I(t), I(o), I(s)), e[8](null), n && n.d(r);
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
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = We(n);
  let {
    svelteInit: u
  } = t;
  const p = S(V(t)), h = S();
  B(e, h, (a) => o(0, s = a));
  const c = S();
  B(e, c, (a) => o(1, i = a));
  const w = [], m = He("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: d,
    subSlotIndex: _
  } = ae() || {}, g = u({
    parent: m,
    props: p,
    target: h,
    slot: c,
    slotKey: y,
    slotIndex: d,
    subSlotIndex: _,
    onDestroy(a) {
      w.push(a);
    }
  });
  qe("$$ms-gr-react-wrapper", g), Be(() => {
    p.set(V(t));
  }), Ke(() => {
    w.forEach((a) => a());
  });
  function E(a) {
    z[a ? "unshift" : "push"](() => {
      s = a, h.set(s);
    });
  }
  function C(a) {
    z[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = U(U({}, t), K(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = K(t), [s, i, h, c, l, u, r, n, E, C];
}
class Xe extends Pe {
  constructor(t) {
    super(), De(this, t, Je, Ve, Ge, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ye(e, t = {}) {
  function o(s) {
    const i = S(), n = new Xe({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
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
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), J({
              createPortal: W,
              node: N
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const Qe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ze(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = $e(o, s), t;
  }, {}) : {};
}
function $e(e, t) {
  return typeof t == "number" && !Qe.includes(e) ? t + "px" : t;
}
function F(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = v.Children.toArray(e._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = F(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...v.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(W(v.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
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
function et(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const X = ne(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = re(), [l, u] = oe([]), {
    forceClone: p
  } = fe(), h = p ? !0 : t;
  return se(() => {
    var y;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), et(n, d), o && d.classList.add(...o.split(" ")), s) {
        const _ = Ze(s);
        Object.keys(_).forEach((g) => {
          d.style[g] = _[g];
        });
      }
    }
    let m = null;
    if (h && window.MutationObserver) {
      let d = function() {
        var C, a, x;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: g,
          clonedElement: E
        } = F(e);
        c = E, u(g), c.style.display = "contents", w(), (x = r.current) == null || x.appendChild(c);
      };
      d();
      const _ = xe(() => {
        d(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (y = r.current) == null || y.appendChild(c);
    return () => {
      var d, _;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, h, o, s, n, i]), v.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function tt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function nt(e, t = !1) {
  try {
    if (ue(e))
      return e;
    if (t && !tt(e))
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
function rt(e, t) {
  return ie(() => nt(e, t), [e, t]);
}
function ot(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const it = Ye(({
  slots: e,
  preview: t,
  ...o
}) => {
  const s = ot(t), i = e["preview.mask"] || e["preview.closeIcon"] || t !== !1, n = rt(s.getContainer);
  return /* @__PURE__ */ L.jsx(de.PreviewGroup, {
    ...o,
    preview: i ? {
      ...s,
      getContainer: n,
      ...e["preview.mask"] || Reflect.has(s, "mask") ? {
        mask: e["preview.mask"] ? /* @__PURE__ */ L.jsx(X, {
          slot: e["preview.mask"]
        }) : s.mask
      } : {},
      closeIcon: e["preview.closeIcon"] ? /* @__PURE__ */ L.jsx(X, {
        slot: e["preview.closeIcon"]
      }) : s.closeIcon
    } : !1
  });
});
export {
  it as ImagePreviewGroup,
  it as default
};
